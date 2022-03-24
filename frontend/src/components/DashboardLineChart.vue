<script>
import Chart from 'chart.js/auto'

export default {
    props: {
        chartId: {
            type: String,
            default: 'myChart'
        },
        labels: {
            default: ['January', 'February', 'March', 'April', 'May', 'June', 'July']
        },
        data: {
            default: [65, 59, 80, 81, 56, 55, 40]
        }
    },
    mounted() {
        Chart.defaults.color = "#888";
        console.log(this.chartId)
        const ctx = document.getElementById(this.chartId).getContext('2d');

        const labels = this.labels;

        const data = {
            labels: labels,
            datasets: [{
                label: 'Total Score',
                data: this.data,
                fill: false,
                backgroundColor: 'rgb(75,192,192)',
                borderColor: 'rgb(75, 192, 192)',
                tension: 0.1
            }]
        };

        const config = {
            type: 'bar',
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

