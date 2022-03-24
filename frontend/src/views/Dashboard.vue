<script>
import DashboardLineChart from '@/components/DashboardLineChart.vue'
import DashboardTable from '@/components/DashboardTable.vue'
import { useUserStore } from '@/stores/UserStore';

export default {
    setup() {
        const UserStore = useUserStore();
        return { UserStore }
    },
    components: {
        DashboardLineChart,
        DashboardTable
    },
    computed: {
        chartLabels() {
            return this.UserStore.decks.map(deck => deck.deck_name);
        },
        chartData() {
            return this.UserStore.decks.map(deck => deck.total_score);
        }
    }
}
</script>

<template>
    <div class="grid grid-rows-2 grid-cols-3 gap-5">
        <DashboardTable v-if="!UserStore.fetchingData" class="col-span-3 row-span-1" />
        <DashboardLineChart v-if="!UserStore.fetchingData" :labels="chartLabels" :data="chartData" class="col-span-3 row-span-1" chart-id="chart-1" />
    </div>
</template>