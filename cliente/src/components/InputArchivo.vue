<template>
<div class="fill-height">
    <v-file-input
    v-model="files"
    color="deep-purple accent-4"
    counter
    label="File input"
    multiple
    placeholder="Select your files"
    prepend-icon="mdi-paperclip"
    outlined
    :show-size="1000"
  >
  </div>
</template>

<script>
export default {
    name: "input-archivo",
    props:[],
    data(){
        return {
            files: null
        };
    },
};
</script>