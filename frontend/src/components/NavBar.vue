<script setup>
import NavBarSwapIcon from '@/components/NavBarSwapIcon.vue';
import NavBarDropDown from '@/components/NavBarDropDown.vue';
</script>

<template>
  <div class="navbar bg-white shadow-2xl rounded-lg sticky top-1 z-50">
    <div class="flex-none">
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
    <div class="flex-1">
      <a class="btn btn-ghost normal-case text-xl">Rahul M</a>
    </div>
    <div class="flex-none gap-x-2">
      <NavBarSwapIcon />
      <NavBarDropDown />
    </div>
  </div>
</template>