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
            class="p-4 overflow-y-auto w-80 bg-slate-100 dark:bg-base-100 text-base-content flex flex-col justify-start flex-nowrap gap-y-10"
        >
            <!-- Sidebar content here -->
            <div class="flex flex-col flex-nowrap">
                <AppLogo />
            </div>

            <div class="flex flex-col flex-nowrap gap-y-6">
                <SideBarItem link="/dashboard" name="Dashboard" />
                <SideBarItem link="/decks" name="Decks" />
                <SideBarItem link="/add-deck" name="Add Deck" />
                <SideBarItem link="/add-card" name="Add Card" />
                <SideBarItem link="/export" name="Deck Exports" />
            </div>
        </div>
    </div>
</template>