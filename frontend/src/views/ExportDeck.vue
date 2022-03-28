<script>
import { useUserStore } from '@/stores/UserStore';
import ExportInfo from '@/components/ExportInfo.vue';

export default {
    components: {
        ExportInfo
    },
    setup(){
        const UserStore = useUserStore();
        return { UserStore };
    },
    computed: {
        pendingJobs() {
            return this.UserStore.backend_jobs.filter(job => job.status == 'pending');
        },
        succeededJobs() {
            return this.UserStore.backend_jobs.filter(job => job.status == 'succeeded');
        }
    }
}
</script>

<template>
<div class="flex flex-col gap-4">
<div class="text-xl font-bold">Succeeded Jobs</div>
<ExportInfo class="cool-shadow" v-for="job in succeededJobs" :job="job" />
</div>
<div class="flex flex-col gap-3">
<div class="text-xl font-bold">Pending Jobs</div>
<ExportInfo v-for="job in pendingJobs" :job="job" />
</div>
</template>