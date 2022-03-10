<script>
import DashboardCard from '@/components/DashboardCard.vue'
import DashboardStat from '@/components/DashboardStat.vue'
export default {
    components: {
        DashboardCard,
        DashboardStat
    }
}
</script>

<template>
    <div class="flex flex-row flex-wrap justify-around gap-y-10 rounded-2xl">
        <!-- <DashboardStat /> -->
        <DashboardCard />
        <DashboardCard />
        <DashboardCard />
        <DashboardCard />
    </div>
</template>