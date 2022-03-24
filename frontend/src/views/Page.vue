<script setup>
import { RouterView } from 'vue-router';
import { useUserStore } from '@/stores/UserStore';
import { useAppStore } from '@/stores/AppStore';
import { useAuthStore } from '@/stores/AuthStore';
import NavBar from '@/components/NavBar.vue'
import SideBar from '@/components/SideBar.vue'
import AppAlertList from '@/components/AppAlertList.vue'
import { reactive, computed, onMounted } from 'vue';

const UserStore = useUserStore()
UserStore.fetchData();

const AppStore = useAppStore()

const AuthStore = useAuthStore();

const state = reactive({ screenWidth: window.innerWidth });

const toggleId = computed(() => {
    return state.screenWidth < 1024 ? 'my-drawer' : '';
})

onMounted(() => {
    window.addEventListener('resize', () => {
        state.screenWidth = window.innerWidth;
        if (window.innerWidth > 1024) {
            const elem = document.getElementsByClassName('drawer-toggle');
            if (elem[0]) {
                elem[0].checked = false;
            }
        }
    })

    const source = AuthStore.eventSource;
    source.addEventListener('Export', (e) => {
        const data = JSON.parse(e.data);
        console.log(data);
        AppStore.pushAlert({
            type: 'success',
            message: data.message
        })
    })
})

</script>

<template>
    <AppAlertList />
    <div
        id="drawer"
        class="drawer h-screen w-full rounded"
        :class="{ 'drawer-mobile': AppStore.showSidebar }"
    >
        <input :id="toggleId" type="checkbox" class="drawer-toggle" />
        <div class="drawer-content bg-slate-200 dark:bg-slate-900">
            <!-- Page content here -->
            <div id="main">
                <div class="flex flex-col justify-start gap-10">
                    <NavBar />
                    <RouterView />
                </div>
            </div>
        </div>
        <SideBar />
    </div>
</template>

<style>
#main {
    position: relative;
    padding: 20px;
}
</style>