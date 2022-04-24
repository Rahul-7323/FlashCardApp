import { defineStore } from "pinia";

export const useAuthStore = defineStore("Auth", {
    state: () => {
        return {
            isAuthenticated: false,
            userId: '',
            authenticationToken: '',
            csrfToken: '',
            dataFetched: false,
            loginErrors: {},
            registerErrors: {},
            eventSource: null,
        }
    },
    getters: {

    },
    actions: {
        getEventSource() {
            this.eventSource = new EventSource(`${import.meta.env.VITE_BACKEND_URL}/stream?channel=${this.userId}`);
        },
        async getCsrfToken(){
            const csrf_token = await fetch(`${import.meta.env.VITE_BACKEND_URL}/login`, {
                        "method": "GET",
                        "headers": {
                            "Content-Type": "application/json"
                        }
                        })
                        .then(response => response.json())
                        .then(data => data.response.csrf_token)
                        .catch(err => {
                        console.error(err);
                        });
            this.csrfToken = csrf_token;
            console.log(csrf_token);
        },
        async register(username, email, password){
            this.registerErrors = {};
            await this.getCsrfToken();
            const data = {
                username:username,
                email: email,
                password: password,
                csrf_token: this.csrfToken
            };
            await fetch(`${import.meta.env.VITE_BACKEND_URL}/register?include_auth_token`, {
                "method": "POST",
                "headers": {
                    "Content-Type": "application/json"
                },
                "body": JSON.stringify(data) 
                })
                .then(response => response.json())
                .then(data => {
                    if(parseInt(data.meta.code) >= 400){
                        this.registerErrors = data.response.errors;
                        throw Error("Unable to register");
                    }
                    return data;
                })
                .then(data => {
                    this.csrfToken = data.response.csrf_token;
                    this.authenticationToken = data.response.user.authentication_token;
                    this.userId = data.response.user.id;
                    this.isAuthenticated = true;
                    this.dataFetched = true;
                    this.getEventSource();

                    const authData = {}
                    authData.csrfToken = this.csrfToken;
                    authData.authenticationToken = this.authenticationToken;
                    authData.userId = this.userId;
                    sessionStorage.flashCardAppAuth = JSON.stringify(authData);
                })
                .catch(err => {
                console.error(err);
                });
            return true;
        },
        async login(email, password){
            this.loginErrors = {};
            await this.getCsrfToken();
            const data = {
                email: email,
                password: password,
                csrf_token: this.csrfToken
            };
            console.log(JSON.stringify(data));
            await fetch(`${import.meta.env.VITE_BACKEND_URL}/login?include_auth_token`, {
                "method": "POST",
                "headers": {
                    "Content-Type": "application/json"
                },
                "body": JSON.stringify(data) 
                })
                .then(response => response.json())
                .then(data => {
                    if(parseInt(data.meta.code) >= 400){
                        this.loginErrors = data.response.errors;
                        throw Error("Unable to login");
                    }
                    console.log("test 1");
                    return data;
                })
                .then(data => {
                    console.log("test 2");
                    this.csrfToken = data.response.csrf_token;
                    this.authenticationToken = data.response.user.authentication_token;
                    this.userId = data.response.user.id;
                    this.isAuthenticated = true;
                    this.dataFetched = true;
                    this.getEventSource();

                    const authData = {}
                    authData.csrfToken = this.csrfToken;
                    authData.authenticationToken = this.authenticationToken;
                    authData.userId = this.userId;
                    sessionStorage.flashCardAppAuth = JSON.stringify(authData);
                    console.log("test 3");
                })
                .catch(err => {
                console.error(err);
                });
        },
        logout() {
            fetch(`${import.meta.env.VITE_BACKEND_URL}/logout`, {
                "method": "POST",
                "headers": {
                    "Content-Type": "application/json"
                }
                })
                .then(response => {
                console.log(response);
                })
                .catch(err => {
                console.error(err);
                });
            this.isAuthenticated = false;
            sessionStorage.clear();
            this.userId = '';
            this.authenticationToken = '';
            this.csrfToken = '';
            this.loginErrors = {};
        },
        authFromSessionStorage() {
            console.log("authFromSessionStorage")
            if(sessionStorage.flashCardAppAuth){
                console.log("sessionStorage present");
                const authData = JSON.parse(sessionStorage.flashCardAppAuth);
                this.csrfToken = authData.csrfToken;
                this.authenticationToken = authData.authenticationToken;
                this.userId = authData.userId;
                this.isAuthenticated = true;
                this.getEventSource();
                return true;
            }
            return false;
        }
    }
})