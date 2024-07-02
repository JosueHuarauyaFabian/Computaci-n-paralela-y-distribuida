document.addEventListener("DOMContentLoaded", function() {
    var ctxLatency = document.getElementById('latencyChart').getContext('2d');
    var latencyChart = new Chart(ctxLatency, {
        type: 'line',
        data: {
            labels: [],
            datasets: [{
                label: 'Latencia',
                data: [],
                borderColor: 'rgba(75, 192, 192, 1)',
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                x: {
                    beginAtZero: true,
                    title: {
                        display: true,
                        text: 'Tiempo'
                    }
                },
                y: {
                    beginAtZero: true,
                    title: {
                        display: true,
                        text: 'Latencia (ms)'
                    }
                }
            }
        }
    });

    var ctxBandwidth = document.getElementById('bandwidthChart').getContext('2d');
    var bandwidthChart = new Chart(ctxBandwidth, {
        type: 'line',
        data: {
            labels: [],
            datasets: [{
                label: 'Ancho de Banda',
                data: [],
                borderColor: 'rgba(153, 102, 255, 1)',
                backgroundColor: 'rgba(153, 102, 255, 0.2)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                x: {
                    beginAtZero: true,
                    title: {
                        display: true,
                        text: 'Tiempo'
                    }
                },
                y: {
                    beginAtZero: true,
                    title: {
                        display: true,
                        text: 'Ancho de Banda (Mbps)'
                    }
                }
            }
        }
    });

    function generateRandomData(previousLatency, previousBandwidth) {
        const latency = Math.max(0, Math.min(100, previousLatency + (Math.random() - 0.5) * 10)); // Simular cambios suaves
        const bandwidth = Math.max(0, Math.min(100, previousBandwidth + (Math.random() - 0.5) * 10)); // Simular cambios suaves
        return { latency, bandwidth };
    }

    let previousLatency = 50; // Valor inicial para la latencia
    let previousBandwidth = 50; // Valor inicial para el ancho de banda

    function updateCharts(data) {
        const { latency, bandwidth } = data;
        const time = new Date().toLocaleTimeString();

        latencyChart.data.labels.push(time);
        latencyChart.data.datasets[0].data.push(latency);
        latencyChart.update();

        bandwidthChart.data.labels.push(time);
        bandwidthChart.data.datasets[0].data.push(bandwidth);
        bandwidthChart.update();
    }

    setInterval(() => {
        const data = generateRandomData(previousLatency, previousBandwidth);
        previousLatency = data.latency;
        previousBandwidth = data.bandwidth;
        updateCharts(data);
    }, 1000);

    document.getElementById('addNodeForm').addEventListener('submit', function(event) {
        event.preventDefault();
        const nodeAddress = document.getElementById('nodeAddress').value;
        fetch('/add_node', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ address: nodeAddress }),
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('Nodo agregado exitosamente');
            } else {
                alert('Error al agregar el nodo');
            }
        });
    });
});
