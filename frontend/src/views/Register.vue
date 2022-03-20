<!--
  This example requires Tailwind CSS v2.0+ 
  
  This example requires some changes to your config:
  
  ```
  // tailwind.config.js
  module.exports = {
    // ...
    plugins: [
      // ...
      require('@tailwindcss/forms'),
    ],
  }
  ```
-->
<script>
import { LockClosedIcon } from '@heroicons/vue/solid'
import { RouterLink, onBeforeRouteLeave } from 'vue-router'
import { useAuthStore } from '@/stores/AuthStore'

export default {
    setup(){
        const AuthStore = useAuthStore();
        return { AuthStore }
    },
    components: {
        LockClosedIcon,
        RouterLink
    },
    data() {
        return {
            username: '',
            email: '',
            password: ''
        }
    },
    methods: {
        async register() {
            if(!this.username){
                alert("Username required")
                return false;
            }
            if(!this.email){
                alert("Email required")
                return false;
            }
            if(!this.password){
                alert("Password required")
                return false
            }
            await this.AuthStore.register(this.username, this.email, this.password);
            if(this.AuthStore.isAuthenticated){
                this.$router.push('/dashboard');
            }
        }
    },
    computed: {
        registerErrors() {
            return this.AuthStore.registerErrors;
        }
    },
    mounted() {
        if(this.AuthStore.isAuthenticated){
            this.$router.push('/dashboard');
        }
    }
}
</script>

<template>
    <!--
    This example requires updating your template:

    ```
    <html class="h-full bg-gray-50">
    <body class="h-full">
    ```
    -->
    <div
        class="w-screen h-screen flex flex-col align-middle items-center justify-center py-12 px-4 sm:px-6 lg:px-8 cool-bg"
    >
        <div class="max-w-md w-full space-y-8 app-card cool-shadow">
            <div>
                <img
                    src="/FlashCardApp-logo.png"
                    alt="FlashCardApp-logo"
                    class="w-full h-20 object-cover rounded-lg shadow-xl bg-black mx-auto"
                />
                <h2
                    class="mt-6 text-center text-3xl font-extrabold text-gray-900 dark:text-slate-100"
                >Register</h2>
            </div>
                <input type="hidden" name="remember" value="true" />
                <div class="rounded-md shadow-sm -space-y-px">
                    <div>
                        <label for="username" class="sr-only">Username</label>
                        <input
                            id="username"
                            name="username"
                            type="username"
                            autocomplete="username"
                            required
                            class="text-gray-900 dark:text-slate-100 appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 bg-base-100 rounded-t-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
                            placeholder="Username"
                            v-model="username"
                        />
                    </div>
                    <div>
                        <label for="email-address" class="sr-only">Email address</label>
                        <input
                            id="email-address"
                            name="email"
                            type="email"
                            autocomplete="email"
                            required
                            class="text-gray-900 dark:text-slate-100 appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 bg-base-100 rounded-t-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
                            placeholder="Email address"
                            v-model="email"
                        />
                    </div>
                    <div>
                        <label for="password" class="sr-only">Password</label>
                        <input
                            id="password"
                            name="password"
                            type="password"
                            autocomplete="current-password"
                            required
                            class="text-gray-900 dark:text-slate-100 appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 bg-base-100 rounded-b-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
                            placeholder="Password"
                            v-model="password"
                        />
                    </div>
                </div>

                <div @click="register()">
                    <button
                        class="btn shadow-md btn-info shadow-blue-400 dark:btn-warning dark:shadow-orange-300 group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-black"
                    >
                        <span class="absolute left-0 inset-y-0 flex items-center pl-3">
                            <LockClosedIcon class="h-5 w-5 text-black" aria-hidden="true" />
                        </span>
                        Register
                    </button>
                </div>
                <div class="ml-4 flex-shrink-0 self-center">or
                  <router-link to="/login" class="font-medium text-indigo-600 hover:text-indigo-500 dark:text-blue-400 dark:hover:text-blue-500"> Login </router-link>
                </div>
                <ul>
                    <li class="alert alert-error rounded-none shadow-lg" v-for="[key,value] in Object.entries(registerErrors)">{{ key }} : {{ value }}</li>
                </ul>
        </div>
    </div>
</template>

