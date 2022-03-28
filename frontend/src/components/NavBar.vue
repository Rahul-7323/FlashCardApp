<script setup>
import NavBarSwapIcon from '@/components/NavBarSwapIcon.vue';
import NavBarDropDown from '@/components/NavBarDropDown.vue';
import { useAppStore } from '@/stores/AppStore'
import { CogIcon } from '@heroicons/vue/outline';

const AppStore = useAppStore();
</script>

<template>
  <div class="navbar bg-base-100 shadow-xl rounded-lg sticky top-1 z-20">
    <div class="navbar-start" @click="AppStore.toggleShowSidebar">
      <label for="my-drawer" class="btn btn-square btn-ghost drawer-button">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 24 24"
          class="inline-block w-5 h-5 stroke-current"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M4 6h16M4 12h16M4 18h16"
          />
        </svg>
      </label>
    </div>
    <div class="navbar-center">
      <a class="btn btn-ghost normal-case text-xl">FlashCardApp</a>
    </div>
    <div class="navbar-end gap-x-2">
      <NavBarSwapIcon />
      <NavBarDropDown />
    </div>
  </div>
</template>