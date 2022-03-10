<script setup>
import { RouterView } from 'vue-router';
import NavBar from '@/components/NavBar.vue'
import SideBar from '@/components/SideBar.vue'
</script>

<template>
    <div class="drawer h-screen drawer-mobile w-full rounded">
        <input id="my-drawer" type="checkbox" class="drawer-toggle" />
        <div class="drawer-content bg-slate-200 dark:bg-slate-900">
            <!-- Page content here -->
            <div id="main">
                <div class="flex flex-col justify-start gap-6">
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