<script>
import DashboardLineChart from '@/components/DashboardLineChart.vue'
import DashboardTable from '@/components/DashboardTable.vue'
export default {
    components: {
        DashboardLineChart,
        DashboardTable
    }
}
</script>

<template>
    <!-- <div class="flex flex-row flex-wrap justify-around gap-6 rounded-2xl w-full">
        <DashboardTable class="w-full" />
        <DashboardLineChart class="w-5/12 h-52" chart-id="chart-1" />
        <DashboardLineChart class="w-5/12 h-52" chart-id="chart-2" />
    </div>-->
    <div class="grid grid-rows-2 grid-cols-3 gap-5">
        <DashboardTable class="col-span-3 md:col-span-2 md:row-span-1" />
        <DashboardLineChart class="col-span-3 md:col-span-1 md:row-span-1" chart-id="chart-1" />
        <DashboardLineChart class="col-span-3 md:col-span-3 md:row-span-1" chart-id="chart-2" />
    </div>
</template>