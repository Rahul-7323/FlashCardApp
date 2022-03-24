<script>
export default {
    props: {
        card: {
            default: {}
        }
    },
    data(){
        return {
            showAnswer: false,
            btnClass: '',
        }
    },
    methods: {
        revealAnswer() {
            this.showAnswer = true;
        }
    },
    emits: ["nextCard"],
}
</script>

<template>
<div class="card bg-base-100 cool-shadow">
  <div class="flex flex-col w-full">
    <div class="p-5 text-lg w-full flex flex-row justify-center break-all"><div><p>{{ card.front }}</p></div></div> 
    <div class="divider m-0"></div> 
    <div v-if="showAnswer" class="p-5 text-lg w-full flex flex-row justify-center break-all"><div><p>{{ card.back }}</p></div></div>
  </div>
</div>
<button v-if="!showAnswer" @click="revealAnswer()" class="btn btn-primary">Reveal Answer</button>
<div v-if="showAnswer">
<div class="card bg-base-100 cool-shadow p-5">
<div class="text-xl text-center font-bold">How did you find the question?</div>
<div class="flex flex-row flex-wrap gap-5 mt-5 justify-center">
    <button class="btn btn-sm btn-success" @click="$emit('nextCard',card.card_id,'easy',3)">Easy</button>
    <button class="btn btn-sm btn-warning" @click="$emit('nextCard',card.card_id,'medium',2)">Medium</button>
    <button class="btn btn-sm btn-error" @click="$emit('nextCard',card.card_id,'hard',1)">Hard</button>
    <button class="btn btn-sm" @click="$emit('nextCard',card.card_id,'null',0)">Don't Know the answer</button>
</div>
</div>
</div>
</template>
