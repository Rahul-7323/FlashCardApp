<template>
    <div class="cool-bg w-screen h-screen flex flex-col">
        <div class="flex flex-col p-10 rounded-xl bg-base-100 cool-shadow">
            <input type="text" placeholder="Type here" class="input w-full max-w-xs" />
            <input type="text" placeholder="Type here" class="input w-full max-w-xs" />
            <router-link to="/dashboard" class="btn btn-primary">Login</router-link>
        </div>
    </div>
</template>