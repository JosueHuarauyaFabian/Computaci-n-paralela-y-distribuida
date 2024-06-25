document.addEventListener("DOMContentLoaded", function() {
    // Crear gráfico de latencia
    var ctxLatency = document.getElementById('latencyChart').getContext('2d');
    var latencyChart = new Chart(ctxLatency, {
        type: 'line',
        data: {
            labels: [], // Etiquetas de tiempo
            datasets: [{
                label: 'Latencia',
                data: [], // Datos de latencia
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

    // Crear gráfico de ancho de banda
    var ctxBandwidth = document.getElementById('bandwidthChart').getContext('2d');
    var bandwidthChart = new Chart(ctxBandwidth, {
        type: 'line',
        data: {
            labels: [], // Etiquetas de tiempo
            datasets: [{
                label: 'Ancho de Banda',
                data: [], // Datos de ancho de banda
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

    // Función para actualizar los datos del gráfico
    function updateCharts(data) {
        const { latency, bandwidth } = data;
        const time = new Date().toLocaleTimeString();

        // Actualizar gráfico de latencia
        latencyChart.data.labels.push(time);
        latencyChart.data.datasets[0].data.push(latency);
        latencyChart.update();

        // Actualizar gráfico de ancho de banda
        bandwidthChart.data.labels.push(time);
        bandwidthChart.data.datasets[0].data.push(bandwidth);
        bandwidthChart.update();
    }

    // Obtener datos del servidor periódicamente
    setInterval(() => {
        fetch('/metrics/metrics')
            .then(response => response.json())
            .then(data => {
                updateCharts(data);
            });
    }, 1000);
});
