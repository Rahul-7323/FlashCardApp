<script>
import { useUserStore } from '@/stores/UserStore'

export default {
    setup() {
        const UserStore = useUserStore();
        return { UserStore }
    },
    data() {
        return {
            webhook_url: ''
        }
    },
    methods: {
        async updateWebhookUrl() {
            if(!this.webhook_url){
                alert("Please enter an url");
                return false;
            }
            await this.UserStore.updateWebhookUrl(this.webhook_url);
            this.webhook_url = '';
        }
    }
}

</script>

<template>
  <div>
    <div class="md:grid md:gap-6">
      
      <div class="mt-5 md:mt-0">
          <div class="shadow sm:rounded-md sm:overflow-hidden">
            <div class="px-4 py-5 bg-white space-y-6 sm:p-6">
              <div>
                <label for="webhook-url" class="block text-sm font-medium text-gray-700"> Webhook URL </label>
                <div class="mt-1">
                  <input v-model="webhook_url" id="webhook-url" name="webhook-url" rows="3" class="shadow-sm focus:ring-indigo-500 focus:border-indigo-500 mt-1 block w-full sm:text-sm border border-gray-300 rounded-md p-3" placeholder="https://discord.com/api/webhooks/" />
                </div>
                <p class="mt-2 text-sm text-gray-500">Discord Webhook URL in order to send messages when some event occurs</p>
              </div>
              
            </div>
            <div class="px-4 py-3 bg-gray-50 sm:px-6">
              <button @click="updateWebhookUrl()" class="btn btn-primary py-0">Update Webhook URL</button>
            </div>
          </div>
      </div>
    </div>
  </div>

  </template>
