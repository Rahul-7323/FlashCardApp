<script>
import DashboardCard from '@/components/DashboardCard.vue'
import DashboardStat from '@/components/DashBoardStat.vue'
import DashBoardStat from '@/components/DashBoardStat.vue'
export default {
    components: {
        DashboardCard,
        DashBoardStat
    }
}
</script>

<template>
    <div class="flex flex-row flex-wrap justify-evenly gap-4 p-5 rounded-2xl">
        <DashBoardStat />
        <DashboardCard />
    </div>
</template>