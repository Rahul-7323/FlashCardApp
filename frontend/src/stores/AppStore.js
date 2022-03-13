import { defineStore } from "pinia";

export const useAppStore = defineStore("App", {
    state: () => {
        return {
            theme: '',
            alerts: [],
            alertCount: 0,
        }
    },
    getters: {
        getAlerts: (state) => {
            return state.alerts.filter(alert => !alert.dismissed)
        }
    },
    actions: {
        getTheme() {
            if (localStorage.flashCardAppTheme) {
                this.theme = localStorage.flashCardAppTheme
            }
            else {
                this.theme = 'dark'
                localStorage.flashCardAppTheme = this.theme
            }
            const htmlElem = document.getElementsByTagName('html')[0];
            htmlElem.setAttribute("data-theme", this.theme);
            if (this.theme === 'dark') {
                htmlElem.classList.add("dark")
            }
        },
        toggleTheme() {
            this.theme = this.theme === 'dark' ? 'light' : 'dark';
            console.log(this.theme);
            const htmlElem = document.getElementsByTagName('html')[0];
            htmlElem.setAttribute("data-theme", this.theme);
            localStorage.flashCardAppTheme = this.theme
            if (this.theme === 'dark') {
                htmlElem.classList.add("dark")
            }
            else {
                htmlElem.classList.remove("dark")
            }
        },
        pushAlert({ type, message }) {
            this.alerts.push({ id: this.alertCount, type: type, message: message, dismissed: false });
            this.alertCount++;
        },
        dismissAlert(id) {
            for (let i = 0; i < this.alerts.length; i++) {
                if (this.alerts[i].id == id) {
                    this.alerts[i].dismissed = true;
                }
            }
        }
    }
})