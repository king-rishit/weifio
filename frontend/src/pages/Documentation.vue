<template>
  <div class="min-h-screen bg-gray-50">
    <!-- Header -->
    <div class="bg-white shadow">
      <div class="max-w-7xl mx-auto px-4 py-8">
        <h1 class="text-4xl font-bold">Documentation</h1>
        <p class="text-gray-600">Learn how to use the Agent Marketplace API</p>
      </div>
    </div>

    <!-- Content -->
    <div class="max-w-7xl mx-auto px-4 py-8">
      <!-- Tabs -->
      <div class="flex gap-4 mb-8 border-b">
        <button
          @click="activeTab = 'api-keys'"
          :class="[
            'pb-3 font-semibold transition',
            activeTab === 'api-keys'
              ? 'border-b-2 border-blue-600 text-blue-600'
              : 'text-gray-600'
          ]"
        >
          API Keys
        </button>
        <button
          @click="activeTab = 'authentication'"
          :class="[
            'pb-3 font-semibold transition',
            activeTab === 'authentication'
              ? 'border-b-2 border-blue-600 text-blue-600'
              : 'text-gray-600'
          ]"
        >
          Authentication
        </button>
        <button
          @click="activeTab = 'guardrails'"
          :class="[
            'pb-3 font-semibold transition',
            activeTab === 'guardrails'
              ? 'border-b-2 border-blue-600 text-blue-600'
              : 'text-gray-600'
          ]"
        >
          Guardrails
        </button>
        <button
          @click="activeTab = 'examples'"
          :class="[
            'pb-3 font-semibold transition',
            activeTab === 'examples'
              ? 'border-b-2 border-blue-600 text-blue-600'
              : 'text-gray-600'
          ]"
        >
          Examples
        </button>
      </div>

      <!-- Tab Content -->
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
        <div class="lg:col-span-2">
          <!-- API Keys Tab -->
          <div v-if="activeTab === 'api-keys'" class="space-y-6">
            <div class="bg-white rounded-lg shadow p-6">
              <h2 class="text-2xl font-bold mb-4">API Keys</h2>
              <p class="text-gray-700 mb-4">
                Every purchase generates a unique API key that allows you to use the agent.
              </p>
              <h3 class="text-lg font-semibold mb-2">Getting Your API Key</h3>
              <ol class="list-decimal list-inside space-y-2 text-gray-700">
                <li>Purchase an agent from the marketplace</li>
                <li>Your API key will be displayed immediately</li>
                <li>Copy and store it securely</li>
                <li>Use it in your application headers</li>
              </ol>
            </div>
          </div>

          <!-- Authentication Tab -->
          <div v-else-if="activeTab === 'authentication'" class="space-y-6">
            <div class="bg-white rounded-lg shadow p-6">
              <h2 class="text-2xl font-bold mb-4">Authentication</h2>
              <p class="text-gray-700 mb-4">Include your API key in the Authorization header:</p>
              <pre class="bg-gray-100 p-4 rounded overflow-x-auto text-sm">Authorization: Bearer YOUR_API_KEY</pre>

              <h3 class="text-lg font-semibold mt-6 mb-2">Verify Key Endpoint</h3>
              <pre class="bg-gray-100 p-4 rounded overflow-x-auto text-sm">GET /purchases/verify-key/{api_key}

Response:
{
  "valid": true,
  "agent_id": 1,
  "agent_name": "GPT-4 Lite",
  "model_name": "gpt-4",
  "guardrails_enabled": true,
  "guardrails_config": "{...}"
}</pre>
            </div>
          </div>

          <!-- Guardrails Tab -->
          <div v-else-if="activeTab === 'guardrails'" class="space-y-6">
            <div class="bg-white rounded-lg shadow p-6">
              <h2 class="text-2xl font-bold mb-4">Guardrails Integration</h2>
              <p class="text-gray-700 mb-4">
                Agents with guardrails enabled validate and monitor outputs for safety.
              </p>

              <h3 class="text-lg font-semibold mb-2">Ollama Guardrails</h3>
              <p class="text-gray-700 mb-3">
                Our marketplace integrates with Ollama guardrails to ensure safe AI outputs.
              </p>

              <h3 class="text-lg font-semibold mb-2">Configuration</h3>
              <p class="text-gray-700 mb-3">
                When an agent has guardrails enabled, its configuration is available through the
                verify endpoint.
              </p>

              <div class="bg-blue-50 border-l-4 border-blue-500 p-4">
                <p class="text-sm text-blue-900">
                  <strong>💡 Tip:</strong> Always verify agent guardrails configuration before
                  using the API in production.
                </p>
              </div>
            </div>
          </div>

          <!-- Examples Tab -->
          <div v-else-if="activeTab === 'examples'" class="space-y-6">
            <div class="bg-white rounded-lg shadow p-6">
              <h2 class="text-2xl font-bold mb-4">API Examples</h2>

              <h3 class="text-lg font-semibold mb-2">JavaScript/Node.js</h3>
              <pre class="bg-gray-100 p-4 rounded overflow-x-auto text-sm mb-4">const apiKey = 'ak_your_api_key_here';

// Verify key
const response = await fetch(
  'http://localhost:8000/purchases/verify-key/' + apiKey
);
const config = await response.json();

console.log(config.agent_name); // Use the agent</pre>

              <h3 class="text-lg font-semibold mb-2">Python</h3>
              <pre class="bg-gray-100 p-4 rounded overflow-x-auto text-sm mb-4">import requests

api_key = 'ak_your_api_key_here'
headers = {'Authorization': f'Bearer {api_key}'}

# Verify key
response = requests.get(
    'http://localhost:8000/purchases/verify-key/' + api_key
)
config = response.json()

print(config['agent_name'])  # Use the agent</pre>

              <h3 class="text-lg font-semibold mb-2">cURL</h3>
              <pre class="bg-gray-100 p-4 rounded overflow-x-auto text-sm">curl -X GET \\
  'http://localhost:8000/purchases/verify-key/ak_your_api_key_here' \\
  -H 'Authorization: Bearer ak_your_api_key_here'</pre>
            </div>
          </div>
        </div>

        <!-- Sidebar -->
        <div>
          <div class="bg-white rounded-lg shadow p-6">
            <h3 class="text-lg font-bold mb-4">Quick Links</h3>
            <ul class="space-y-2">
              <li>
                <router-link to="/" class="text-blue-600 hover:underline"> → Browse Marketplace </router-link>
              </li>
              <li>
                <router-link to="/purchases" class="text-blue-600 hover:underline">
                  → My Purchases
                </router-link>
              </li>
            </ul>

            <div class="mt-6 p-4 bg-blue-50 rounded">
              <p class="text-sm text-gray-700">
                <strong>API Base:</strong>
                <br />
                <code class="text-xs">http://localhost:8000</code>
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { RouterLink } from 'vue-router'

const activeTab = ref('api-keys')
</script>
