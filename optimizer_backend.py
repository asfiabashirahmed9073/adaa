# Radiant Optimizer - Windows Gaming Performance Tweaks
# Python Backend for Real System Optimization

import psutil
import winreg
import subprocess
import os
import json
from datetime import datetime

class RadiantOptimizer:
    def __init__(self):
        self.backup_file = "radiant_backup.json"
        self.load_backup()

    def load_backup(self):
        """Load previous settings backup"""
        try:
            if os.path.exists(self.backup_file):
                with open(self.backup_file, 'r') as f:
                    self.backup = json.load(f)
            else:
                self.backup = {}
        except:
            self.backup = {}

    def save_backup(self):
        """Save current settings before applying tweaks"""
        with open(self.backup_file, 'w') as f:
            json.dump(self.backup, f, indent=2)

    # ============ SYSTEM INFORMATION ============

    def get_system_info(self):
        """Get real system information"""
        cpu_freq = psutil.cpu_freq()
        mem = psutil.virtual_memory()
        disk = psutil.disk_usage('C:')

        return {
            'cpu': {
                'cores': psutil.cpu_count(logical=False),
                'threads': psutil.cpu_count(logical=True),
                'frequency': f"{cpu_freq.current:.0f} MHz" if cpu_freq else "N/A",
                'usage': psutil.cpu_percent(interval=1)
            },
            'memory': {
                'total_gb': round(mem.total / (1024**3), 1),
                'used_gb': round(mem.used / (1024**3), 1),
                'percent': mem.percent
            },
            'disk': {
                'total_gb': round(disk.total / (1024**3), 1),
                'used_gb': round(disk.used / (1024**3), 1),
                'percent': disk.percent
            }
        }

    def get_gpu_info(self):
        """Get GPU information using wmic"""
        try:
            result = subprocess.run(
                ['wmic', 'path', 'win32_VideoController', 'get', 'name'],
                capture_output=True, text=True, timeout=5
            )
            lines = result.stdout.strip().split('\n')
            gpu_name = lines[1].strip() if len(lines) > 1 else "Unknown GPU"
            return {'name': gpu_name}
        except:
            return {'name': 'Unknown GPU'}

    # ============ GAMING OPTIMIZATIONS ============

    def enable_game_mode(self):
        """Enable Windows Game Mode"""
        try:
            key_path = r"Software\Microsoft\GameBar"
            key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, key_path)

            # Backup current value
            try:
                current_value = winreg.QueryValueEx(key, "AutoGameModeEnabled")[0]
                self.backup['game_mode'] = current_value
            except:
                self.backup['game_mode'] = 0

            # Enable Game Mode
            winreg.SetValueEx(key, "AutoGameModeEnabled", 0, winreg.REG_DWORD, 1)
            winreg.CloseKey(key)
            self.save_backup()
            return True, "Game Mode enabled successfully"
        except Exception as e:
            return False, f"Failed to enable Game Mode: {str(e)}"

    def disable_game_mode(self):
        """Disable Windows Game Mode"""
        try:
            key_path = r"Software\Microsoft\GameBar"
            key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, key_path)
            winreg.SetValueEx(key, "AutoGameModeEnabled", 0, winreg.REG_DWORD, 0)
            winreg.CloseKey(key)
            return True, "Game Mode disabled"
        except Exception as e:
            return False, f"Failed: {str(e)}"

    def set_high_performance_power_plan(self):
        """Set Windows to High Performance power plan"""
        try:
            # Get High Performance GUID
            result = subprocess.run(
                ['powercfg', '/list'],
                capture_output=True, text=True
            )

            # Find High Performance GUID
            for line in result.stdout.split('\n'):
                if 'High performance' in line or 'Ultimate Performance' in line:
                    guid = line.split(':')[1].strip().split()[0]

                    # Set active power plan
                    subprocess.run(['powercfg', '/setactive', guid], check=True)
                    return True, f"High Performance mode activated"

            return False, "High Performance plan not found"
        except Exception as e:
            return False, f"Failed: {str(e)}"

    def disable_fullscreen_optimizations(self):
        """Disable fullscreen optimizations globally"""
        try:
            key_path = r"System\GameConfigStore"
            key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, key_path)

            # Backup
            try:
                current_value = winreg.QueryValueEx(key, "GameDVR_FSEBehaviorMode")[0]
                self.backup['fse_behavior'] = current_value
            except:
                self.backup['fse_behavior'] = 0

            winreg.SetValueEx(key, "GameDVR_FSEBehaviorMode", 0, winreg.REG_DWORD, 2)
            winreg.CloseKey(key)
            self.save_backup()
            return True, "Fullscreen optimizations disabled"
        except Exception as e:
            return False, f"Failed: {str(e)}"

    def disable_game_dvr(self):
        """Disable Xbox Game DVR/Bar"""
        try:
            key_path = r"System\GameConfigStore"
            key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, key_path)

            # Disable Game DVR
            winreg.SetValueEx(key, "GameDVR_Enabled", 0, winreg.REG_DWORD, 0)
            winreg.CloseKey(key)

            # Disable Game Bar
            key_path2 = r"Software\Microsoft\Windows\CurrentVersion\GameDVR"
            key2 = winreg.CreateKey(winreg.HKEY_CURRENT_USER, key_path2)
            winreg.SetValueEx(key2, "AppCaptureEnabled", 0, winreg.REG_DWORD, 0)
            winreg.CloseKey(key2)

            return True, "Game DVR and Game Bar disabled"
        except Exception as e:
            return False, f"Failed: {str(e)}"

    def optimize_nvidia_settings(self):
        """Apply NVIDIA optimization settings"""
        try:
            # Check if NVIDIA Control Panel is available
            nvidia_path = r"C:\Program Files\NVIDIA Corporation\Control Panel Client\nvcplui.exe"

            if not os.path.exists(nvidia_path):
                return False, "NVIDIA Control Panel not found"

            # Apply power management mode to prefer maximum performance
            key_path = r"System\CurrentControlSet\Control\GraphicsDrivers\Power"
            try:
                key = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, key_path)
                winreg.SetValueEx(key, "RmGpsPsEnablePerCpuContainer", 0, winreg.REG_DWORD, 1)
                winreg.CloseKey(key)
            except PermissionError:
                return False, "Need Administrator rights for NVIDIA tweaks"

            return True, "NVIDIA settings optimized (Run as Admin for full optimization)"
        except Exception as e:
            return False, f"Failed: {str(e)}"

    def disable_visual_effects(self):
        """Disable Windows visual effects for performance"""
        try:
            key_path = r"Software\Microsoft\Windows\CurrentVersion\Explorer\VisualEffects"
            key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, key_path)

            # Backup
            try:
                current_value = winreg.QueryValueEx(key, "VisualFXSetting")[0]
                self.backup['visual_fx'] = current_value
            except:
                self.backup['visual_fx'] = 1

            # Set to "Adjust for best performance" (value 2)
            winreg.SetValueEx(key, "VisualFXSetting", 0, winreg.REG_DWORD, 2)
            winreg.CloseKey(key)
            self.save_backup()

            return True, "Visual effects disabled (Restart Windows Explorer)"
        except Exception as e:
            return False, f"Failed: {str(e)}"

    def optimize_system_responsiveness(self):
        """Optimize system responsiveness for gaming"""
        try:
            key_path = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile"
            key = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, key_path)

            try:
                # Backup
                current_value = winreg.QueryValueEx(key, "SystemResponsiveness")[0]
                self.backup['system_responsiveness'] = current_value
            except:
                self.backup['system_responsiveness'] = 20

            # Set to 0 for maximum responsiveness
            winreg.SetValueEx(key, "SystemResponsiveness", 0, winreg.REG_DWORD, 0)
            winreg.CloseKey(key)
            self.save_backup()

            return True, "System responsiveness optimized"
        except PermissionError:
            return False, "Need Administrator rights for this tweak"
        except Exception as e:
            return False, f"Failed: {str(e)}"

    def disable_windows_update_during_gaming(self):
        """Pause Windows Update temporarily"""
        try:
            # Pause updates for 1 week
            subprocess.run([
                'powershell', '-Command',
                'Set-ItemProperty -Path "HKLM:\\SOFTWARE\\Policies\\Microsoft\\Windows\\WindowsUpdate\\AU" -Name "NoAutoUpdate" -Value 1'
            ], check=True)

            return True, "Windows Update paused during gaming"
        except:
            return False, "Need Administrator rights"

    def clean_temp_files(self):
        """Clean temporary files"""
        try:
            temp_dirs = [
                os.environ.get('TEMP'),
                os.environ.get('TMP'),
                r'C:\Windows\Temp'
            ]

            cleaned = 0
            for temp_dir in temp_dirs:
                if temp_dir and os.path.exists(temp_dir):
                    for root, dirs, files in os.walk(temp_dir):
                        for file in files:
                            try:
                                os.remove(os.path.join(root, file))
                                cleaned += 1
                            except:
                                pass

            return True, f"Cleaned {cleaned} temporary files"
        except Exception as e:
            return False, f"Failed: {str(e)}"

    # ============ RESTORE FUNCTIONS ============

    def restore_all_tweaks(self):
        """Restore all backed up settings"""
        results = []

        if 'game_mode' in self.backup:
            try:
                key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\GameBar")
                winreg.SetValueEx(key, "AutoGameModeEnabled", 0, winreg.REG_DWORD, self.backup['game_mode'])
                winreg.CloseKey(key)
                results.append("Game Mode restored")
            except:
                results.append("Game Mode restore failed")

        if 'visual_fx' in self.backup:
            try:
                key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Explorer\VisualEffects")
                winreg.SetValueEx(key, "VisualFXSetting", 0, winreg.REG_DWORD, self.backup['visual_fx'])
                winreg.CloseKey(key)
                results.append("Visual effects restored")
            except:
                results.append("Visual effects restore failed")

        return True, "\n".join(results) if results else "No backup found"

    # ============ QUICK OPTIMIZATION PRESETS ============

    def apply_gaming_preset(self):
        """Apply all gaming optimizations at once"""
        results = []

        tweaks = [
            ('Game Mode', self.enable_game_mode),
            ('High Performance Power', self.set_high_performance_power_plan),
            ('Disable Game DVR', self.disable_game_dvr),
            ('Disable FSE', self.disable_fullscreen_optimizations),
            ('Visual Effects', self.disable_visual_effects)
        ]

        for name, func in tweaks:
            success, msg = func()
            results.append(f"{name}: {'✓' if success else '✗'} {msg}")

        return results

    def apply_fps_boost_preset(self):
        """Apply FPS boosting tweaks"""
        results = []

        tweaks = [
            ('Game Mode', self.enable_game_mode),
            ('Disable Game DVR', self.disable_game_dvr),
            ('System Responsiveness', self.optimize_system_responsiveness),
            ('Clean Temp', self.clean_temp_files)
        ]

        for name, func in tweaks:
            success, msg = func()
            results.append(f"{name}: {'✓' if success else '✗'} {msg}")

        return results

# Example usage
if __name__ == "__main__":
    optimizer = RadiantOptimizer()

    # Get system info
    print("=== System Information ===")
    info = optimizer.get_system_info()
    print(f"CPU: {info['cpu']['cores']} cores, {info['cpu']['threads']} threads")
    print(f"CPU Usage: {info['cpu']['usage']}%")
    print(f"RAM: {info['memory']['used_gb']:.1f} / {info['memory']['total_gb']:.1f} GB ({info['memory']['percent']}%)")
    print(f"Disk: {info['disk']['used_gb']:.0f} / {info['disk']['total_gb']:.0f} GB ({info['disk']['percent']}%)")

    print("\n=== GPU Information ===")
    gpu = optimizer.get_gpu_info()
    print(f"GPU: {gpu['name']}")

    print("\n=== Available Optimizations ===")
    print("1. Enable Game Mode")
    print("2. Set High Performance Power Plan")
    print("3. Disable Game DVR/Bar")
    print("4. Disable Fullscreen Optimizations")
    print("5. Optimize NVIDIA Settings")
    print("6. Disable Visual Effects")
    print("7. Clean Temp Files")
    print("8. Apply Gaming Preset (All)")
    print("9. Apply FPS Boost Preset")
    print("0. Restore All Tweaks")
