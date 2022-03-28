<script>
export default{
    props: ['job'],
}
</script>

<template>
<div class="alert shadow-lg">
  <div>
    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" class="stroke-info flex-shrink-0 w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
    <div>
      <h3 class="font-bold">{{ job.deck_name }}</h3>
      <div class="text-xs">{{ job.job_id }}</div>
    </div>
  </div>
  <div class="flex-none">
    <a v-if="job.status == 'succeeded'" :href="job.url" class="btn btn-sm" target="_blank" download>Download</a>
  </div>
</div>
</template>