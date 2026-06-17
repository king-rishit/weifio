<template>
  <div class="bg-white rounded-lg shadow-md hover:shadow-lg transition-shadow overflow-hidden">
    <!-- Agent Image -->
    <div class="w-full h-48 bg-gradient-to-r from-blue-400 to-purple-500 flex items-center justify-center">
      <img v-if="agent.image_url" :src="agent.image_url" :alt="agent.name" class="w-full h-full object-cover" />
      <div v-else class="text-4xl">🤖</div>
    </div>

    <!-- Card Content -->
    <div class="p-4">
      <!-- Agent Name -->
      <h3 class="text-xl font-bold mb-2">{{ agent.name }}</h3>

      <!-- Description -->
      <p class="text-gray-600 text-sm mb-3 line-clamp-2">{{ agent.description }}</p>

      <!-- Model Info -->
      <div class="text-xs text-gray-500 mb-3">
        <p>Model: {{ agent.model_name }}</p>
        <p v-if="agent.guardrails_enabled" class="text-green-600 font-semibold">✓ Guardrails Enabled</p>
      </div>

      <!-- Rating -->
      <div class="flex items-center gap-2 mb-3">
        <div class="flex items-center gap-1">
          <span v-for="i in 5" :key="i" class="text-sm">
            {{ i <= Math.round(agent.rating) ? '★' : '☆' }}
          </span>
        </div>
        <span class="text-sm font-semibold">{{ agent.rating.toFixed(1) }}</span>
        <span class="text-xs text-gray-500">({{ agent.total_reviews }} reviews)</span>
      </div>

      <!-- Price and Actions -->
      <div class="flex items-center justify-between">
        <div>
          <span class="text-2xl font-bold text-blue-600">${{ agent.price }}</span>
          <span v-if="agent.price === 0" class="text-sm text-green-600 ml-2">Free</span>
        </div>
        <div class="flex gap-2">
          <button
            @click="$emit('view-details', agent.id)"
            class="px-3 py-2 bg-gray-100 hover:bg-gray-200 rounded text-sm font-medium transition"
          >
            Details
          </button>
          <button
            @click="$emit('purchase', agent.id)"
            class="px-3 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded text-sm font-medium transition"
          >
            Buy
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  agent: {
    type: Object,
    required: true
  }
})

defineEmits(['purchase', 'view-details'])
</script>
