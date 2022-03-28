<script setup>
import { useAuthStore } from '@/stores/AuthStore';
import { CogIcon } from '@heroicons/vue/outline';

const AuthStore = useAuthStore();
</script>

<template>
    <div class="dropdown dropdown-end">
        <label tabindex="0" class="btn btn-ghost btn-circle">
            <div class="w-10 p-1 rounded-full">
                <CogIcon/>
            </div>
        </label>
        <ul
            tabindex="0"
            class="mt-3 p-2 shadow menu menu-compact dropdown-content bg-base-100 rounded-box w-52"
        >
            <li>
                <router-link to="/userinfo">User Info</router-link>
            </li>
            <li>
                <router-link to="/update_webhook">Update Webhook</router-link>
            </li>
            <li>
                <router-link to="/login" @click="AuthStore.logout()">Logout</router-link>
            </li>
        </ul>
    </div>
</template>