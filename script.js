// Radiant Optimizer - PC Performance & Tweaks Application
// Main JavaScript for navigation, live monitoring, and system metrics

// Home Page Content Template
const homePageContent = `
    <div class="page-header">
        <h2>Your <span class="highlight">PC</span></h2>
        <p class="subtitle">Hardware, usage, and benchmark results.</p>
    </div>

    <div class="content-grid">
        <div class="system-info-col">
            <div class="monitoring-controls">
                <button class="btn-secondary btn-sm" onclick="scanPC()">Scan this PC</button>
                <label class="switch-label">
                    <input type="checkbox" id="liveMonitoring" checked>
                    <span class="switch"></span>
                    <span>Live monitoring</span>
                </label>
            </div>

            <div class="info-grid">
                ${generateSystemCards()}
            </div>

            ${generateChartSection()}
        </div>

        <div class="benchmark-col">
            ${generateBenchmarkCard()}
        </div>
    </div>
`;

// Generate system information cards
function generateSystemCards() {
    return `
        <div class="info-card">
            <div class="card-header">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <rect x="2" y="2" width="20" height="8" rx="2" ry="2"></rect>
                    <rect x="2" y="14" width="20" height="8" rx="2" ry="2"></rect>
                </svg>
                <div>
                    <h3>System board</h3>
                    <p class="card-subtitle">PRO X670E-P WIFI (MS-7E70)</p>
                </div>
            </div>
            <div class="card-stats">
                <div class="stat-item">
                    <div class="stat-value">8</div>
                    <div class="stat-label">CPU cores</div>
                </div>
                <div class="stat-item">
                    <div class="stat-value">16</div>
                    <div class="stat-label">Threads</div>
                </div>
            </div>
        </div>

        <div class="info-card">
            <div class="card-header">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <rect x="2" y="7" width="20" height="15" rx="2" ry="2"></rect>
                </svg>
                <div>
                    <h3>Graphics</h3>
                    <p class="card-subtitle">NVIDIA GeForce RTX 4090</p>
                </div>
            </div>
            <div class="usage-stat">
                <div class="usage-value"><span id="gpuUsage">16.0</span> <span class="usage-unit">%</span></div>
                <div class="usage-label">GPU usage</div>
                <div class="progress-bar">
                    <div class="progress-fill" id="gpuProgress" style="width: 16%"></div>
                </div>
            </div>
        </div>

        <div class="info-card">
            <div class="card-header">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <rect x="4" y="4" width="16" height="16" rx="2" ry="2"></rect>
                    <rect x="9" y="9" width="6" height="6"></rect>
                </svg>
                <div>
                    <h3>Processor</h3>
                    <p class="card-subtitle">AMD Ryzen 7 9800X3D 8-Core</p>
                </div>
            </div>
            <div class="usage-stat">
                <div class="usage-value"><span id="cpuUsage">25.7</span> <span class="usage-unit">%</span></div>
                <div class="usage-label">CPU usage</div>
                <div class="progress-bar">
                    <div class="progress-fill" id="cpuProgress" style="width: 25.7%"></div>
                </div>
            </div>
        </div>

        <div class="info-card">
            <div class="card-header">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <rect x="3" y="4" width="18" height="16" rx="2" ry="2"></rect>
                </svg>
                <div>
                    <h3>Memory</h3>
                    <p class="card-subtitle">64 GB installed</p>
                </div>
            </div>
            <div class="usage-stat">
                <div class="usage-value"><span id="memUsage">23</span> <span class="usage-unit">/ 61 GB</span></div>
                <div class="usage-label">Memory usage</div>
                <div class="progress-bar">
                    <div class="progress-fill" id="memProgress" style="width: 37.7%"></div>
                </div>
            </div>
        </div>

        <div class="info-card">
            <div class="card-header">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <ellipse cx="12" cy="5" rx="9" ry="3"></ellipse>
                    <path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3"></path>
                </svg>
                <div>
                    <h3>Storage</h3>
                    <p class="card-subtitle">C: Seagate ZP2000GM34004</p>
                </div>
            </div>
            <div class="usage-stat">
                <div class="usage-value">915 <span class="usage-unit">/ 932 GB</span></div>
                <div class="usage-label">Storage usage</div>
                <div class="progress-bar">
                    <div class="progress-fill" style="width: 98.2%"></div>
                </div>
            </div>
        </div>

        <div class="info-card">
            <div class="card-header">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M5 12.55a11 11 0 0 1 14.08 0"></path>
                    <path d="M8.53 16.11a6 6 0 0 1 6.95 0"></path>
                </svg>
                <div>
                    <h3>Network</h3>
                </div>
            </div>
            <div class="network-stats">
                <div class="network-stat-item">
                    <div class="network-value"><span id="downloadSpeed">0.0</span> <span class="network-unit">Mbps</span></div>
                    <div class="network-label">Download</div>
                </div>
                <div class="network-stat-item">
                    <div class="network-value"><span id="uploadSpeed">0.0</span> <span class="network-unit">Mbps</span></div>
                    <div class="network-label">Upload</div>
                </div>
            </div>
        </div>
    `;
}

// Generate chart section
function generateChartSection() {
    return `
        <div class="chart-section">
            <div class="chart-header">
                <h3>More readings</h3>
                <span class="monitoring-status">Monitoring on</span>
            </div>
            <div class="chart-card">
                <div class="chart-title">
                    <span>Temperature history</span>
                    <div class="chart-legends">
                        <span class="legend-item">
                            <span class="legend-color" style="background: #4F7CFF"></span>
                            CPU: Unavailable
                        </span>
                        <span class="legend-item">
                            <span class="legend-color" style="background: #00D9FF"></span>
                            GPU: 43°C
                        </span>
                    </div>
                </div>
                <div class="chart-container">
                    <canvas id="temperatureChart"></canvas>
                </div>
                <div class="chart-timeline">
                    <span>60m ago</span>
                    <span>Now</span>
                </div>
            </div>

            <div class="system-readings">
                <h4>Current system</h4>
                <p class="readings-subtitle">Additional live readings</p>
                <div class="readings-grid">
                    <div class="reading-item">
                        <span class="reading-label">Uptime</span>
                        <span class="reading-value">Jul 3h 49m</span>
                    </div>
                    <div class="reading-item">
                        <span class="reading-label">Processes</span>
                        <span class="reading-value">262</span>
                    </div>
                    <div class="reading-item">
                        <span class="reading-label">Download</span>
                        <span class="reading-value">0.0 Mbps</span>
                    </div>
                    <div class="reading-item">
                        <span class="reading-label">Upload</span>
                        <span class="reading-value">0.0 Mbps</span>
                    </div>
                </div>
            </div>
        </div>
    `;
}

// Generate benchmark card
function generateBenchmarkCard() {
    return `
        <div class="benchmark-card">
            <div class="benchmark-header">
                <div class="benchmark-title">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M18 20V10"></path>
                        <path d="M12 20V4"></path>
                        <path d="M6 20v-6"></path>
                    </svg>
                    <span>PC BENCHMARK</span>
                </div>
            </div>

            <div class="benchmark-score">
                <div class="score-badge">
                    <div class="badge-text">AT HIGHEST</div>
                    <div class="brand-logo">Radiant</div>
                    <div class="star-icon">
                        <svg viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M50 10 L61.8 38.2 L92.7 42.7 L71.4 63.1 L76.3 93.8 L50 78.5 L23.7 93.8 L28.6 63.1 L7.3 42.7 L38.2 38.2 Z" fill="#4F7CFF" stroke="#6B8FFF" stroke-width="2"/>
                        </svg>
                    </div>
                </div>
                <div class="score-value">5,264 <span class="score-unit">POINTS</span></div>
            </div>

            <button class="btn-benchmark" onclick="runBenchmark()">
                <span>Run benchmark</span>
            </button>
            <p class="benchmark-note">Measure your performance. Keeps your settings.</p>

            <div class="benchmark-checklist">
                <h4>▶ Before you run</h4>
                <ul>
                    <li>Close resource-intensive apps</li>
                    <li>Use performance mode</li>
                    <li>Plug in your laptop</li>
                </ul>
            </div>

            <div class="benchmark-history">
                <h4>LAST FIVE</h4>
                <div class="history-list">
                    ${generateBenchmarkHistory()}
                </div>
            </div>
        </div>
    `;
}

// Generate benchmark history
function generateBenchmarkHistory() {
    const history = [
        { date: 'Oct 29, 9:33 AM', score: 5124 },
        { date: 'Oct 28, 11:09 PM', score: 5264 },
        { date: 'Oct 28, 9:48 PM', score: 5179 },
        { date: 'Oct 28, 9:42 PM', score: 5179 }
    ];

    return history.map(item => `
        <div class="history-item">
            <div class="history-icon">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M18 20V10"></path>
                    <path d="M12 20V4"></path>
                    <path d="M6 20v-6"></path>
                </svg>
            </div>
            <div class="history-info">
                <span class="history-name">Radiant</span>
                <span class="history-date">${item.date}</span>
            </div>
            <span class="history-score">${item.score.toLocaleString()}</span>
        </div>
    `).join('');
}

// Navigation handler
function initNavigation() {
    const navItems = document.querySelectorAll('.nav-item');
    const content = document.getElementById('content');

    navItems.forEach(item => {
        item.addEventListener('click', () => {
            navItems.forEach(nav => nav.classList.remove('active'));
            item.classList.add('active');

            const page = item.dataset.page;
            loadPage(page);
        });
    });

    loadPage('home');
}

// Load page content
function loadPage(page) {
    const content = document.getElementById('content');

    switch(page) {
        case 'home':
            content.innerHTML = homePageContent;
            initHomePageFeatures();
            break;
        case 'optimize':
            content.innerHTML = '<div class="page-header"><h2>Diagnose & <span class="highlight">Optimize</span></h2><p class="subtitle">Coming soon...</p></div>';
            break;
        case 'tweaks':
            content.innerHTML = '<div class="page-header"><h2>System <span class="highlight">Tweaks</span></h2><p class="subtitle">Coming soon...</p></div>';
            break;
        default:
            content.innerHTML = '<div class="page-header"><h2><span class="highlight">Coming Soon</span></h2></div>';
    }
}

// Initialize home page features
function initHomePageFeatures() {
    const liveMonitoring = document.getElementById('liveMonitoring');
    if (liveMonitoring) {
        liveMonitoring.addEventListener('change', (e) => {
            if (e.target.checked) {
                startLiveMonitoring();
            } else {
                stopLiveMonitoring();
            }
        });

        if (liveMonitoring.checked) {
            startLiveMonitoring();
        }
    }

    initTemperatureChart();
}

let monitoringInterval;

// Start live monitoring
function startLiveMonitoring() {
    updateSystemMetrics();
    monitoringInterval = setInterval(() => {
        updateSystemMetrics();
    }, 2000);
}

// Stop live monitoring
function stopLiveMonitoring() {
    if (monitoringInterval) {
        clearInterval(monitoringInterval);
    }
}

// Update system metrics with simulated data
function updateSystemMetrics() {
    const cpuUsage = (Math.random() * 30 + 15).toFixed(1);
    const cpuElement = document.getElementById('cpuUsage');
    const cpuProgress = document.getElementById('cpuProgress');
    if (cpuElement) cpuElement.textContent = cpuUsage;
    if (cpuProgress) cpuProgress.style.width = cpuUsage + '%';

    const gpuUsage = (Math.random() * 25 + 10).toFixed(1);
    const gpuElement = document.getElementById('gpuUsage');
    const gpuProgress = document.getElementById('gpuProgress');
    if (gpuElement) gpuElement.textContent = gpuUsage;
    if (gpuProgress) gpuProgress.style.width = gpuUsage + '%';

    const memUsage = Math.floor(Math.random() * 10 + 20);
    const memElement = document.getElementById('memUsage');
    const memProgress = document.getElementById('memProgress');
    if (memElement) memElement.textContent = memUsage;
    if (memProgress) memProgress.style.width = ((memUsage / 61) * 100).toFixed(1) + '%';

    const download = (Math.random() * 5).toFixed(1);
    const upload = (Math.random() * 2).toFixed(1);
    const downloadElement = document.getElementById('downloadSpeed');
    const uploadElement = document.getElementById('uploadSpeed');
    if (downloadElement) downloadElement.textContent = download;
    if (uploadElement) uploadElement.textContent = upload;
}

// Run benchmark simulation
function runBenchmark() {
    const score = Math.floor(Math.random() * 500 + 5000);
    alert(`Benchmark completed!\n\nYour Score: ${score.toLocaleString()} points\n\nPerformance: Excellent`);
}

// Scan PC function
function scanPC() {
    alert('Scanning your PC for optimization opportunities...\n\nScan complete! No issues found.');
}

// Initialize temperature chart
function initTemperatureChart() {
    const canvas = document.getElementById('temperatureChart');
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    canvas.width = canvas.offsetWidth;
    canvas.height = canvas.offsetHeight;

    ctx.strokeStyle = 'rgba(79, 124, 255, 0.1)';
    ctx.lineWidth = 1;

    for (let i = 0; i <= 4; i++) {
        const y = (canvas.height / 4) * i;
        ctx.beginPath();
        ctx.moveTo(0, y);
        ctx.lineTo(canvas.width, y);
        ctx.stroke();
    }

    ctx.strokeStyle = '#00D9FF';
    ctx.lineWidth = 2;
    ctx.beginPath();

    const points = 60;
    for (let i = 0; i < points; i++) {
        const x = (canvas.width / points) * i;
        const y = canvas.height / 2 + Math.sin(i / 5) * 20 + Math.random() * 10;

        if (i === 0) {
            ctx.moveTo(x, y);
        } else {
            ctx.lineTo(x, y);
        }
    }
    ctx.stroke();
}

// Initialize app
document.addEventListener('DOMContentLoaded', () => {
    initNavigation();
});
