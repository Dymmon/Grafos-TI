<template>
  <div
    style="width: 150px; display: flex; flex-direction: column; align-items: center; justify-content: center;"
  >
    <div class="column is-12">
      <img style="border-radius: 100px; width: 100%;" :src="imagen" />
    </div>
    <div
      class="column is-12 has-text-centered has-text-weight-bold is-paddingless"
    >
      <span style="font-size: 16px">{{ nombre }}</span>
    </div>
  </div>
</template>

<script>
export default {
  name: "Persona",
  props: ["nombre", "imagen", "redes"],
  data: () => ({}),
};
</script>