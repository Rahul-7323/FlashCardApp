<script>
import Chart from 'chart.js/auto'

export default {
    props: {
        chartId: {
            type: String,
            default: 'myChart'
        }
    },
    mounted() {
        Chart.defaults.color = "#888";
        console.log(this.chartId)
        const ctx = document.getElementById(this.chartId).getContext('2d');

        const labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July'];

        const data = {
            labels: labels,
            datasets: [{
                label: 'My First Dataset',
                data: [65, 59, 80, 81, 56, 55, 40],
                fill: false,
                borderColor: 'rgb(75, 192, 192)',
                tension: 0.1
            }]
        };

        const config = {
            type: 'line',
            data: data,
            options: {
                maintainAspectRatio: false,
            }
        };

        const myChart = new Chart(ctx, config);
    }
}
</script>

<template>
    <div class="bg-base-100 cool-shadow rounded-lg p-5">
        <canvas :id="chartId"></canvas>
    </div>
</template>

