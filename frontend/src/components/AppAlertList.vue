<script>
import AppAlert from '@/components/AppAlert.vue'
import { useAppStore } from '@/stores/AppStore'

export default {
    components: {
        AppAlert,
    },
    setup() {
        const AppStore = useAppStore();
        return { AppStore }
    },
    computed: {
        undismissedAlerts() {
            return this.AppStore.getAlerts;
        }
    }
}
</script>

<template>
    <div class="fixed bottom-6 left-0 z-30">
        <div class="flex flex-col w-screen gap-6">
            <AppAlert
                v-for="alert in undismissedAlerts"
                :id="alert.id"
                :alert-type="alert.type"
                :key="alert.id"
                @dismiss-alert="(id) => AppStore.dismissAlert(id)"
            >{{ alert.message }}</AppAlert>
        </div>
    </div>
</template>