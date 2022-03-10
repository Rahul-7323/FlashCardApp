<script>
import SideBarItem from "@/components/SideBarItem.vue"
import AppLogo from "@/components/AppLogo.vue"
export default {
    components: {
        SideBarItem,
        AppLogo
    }
}
</script>

<template>
    <div class="drawer-side">
        <label for="my-drawer" class="drawer-overlay"></label>
        <div
            class="p-4 overflow-y-auto w-80 bg-slate-100 dark:bg-base-100 text-base-content flex flex-col justify-start flex-nowrap gap-y-16"
        >
            <!-- Sidebar content here -->
            <div class="flex flex-col flex-nowrap">
                <AppLogo />
            </div>

            <div class="flex flex-col flex-nowrap gap-y-4">
                <SideBarItem link="/dashboard" name="Dashboard" />
                <SideBarItem link="/review" name="Review" />
            </div>
        </div>
    </div>
</template>