import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },


  server: {

    
    proxy: {
      '/api': 'http://localhost:5000',  // Adjust the path if your Flask API is served elsewhere
    },
  },
  build: {
    outDir: '../static/assets',  // Ensures the build goes directly to Flask static folder
  },
  rollupOptions: {
    output: {
      manualChunks: undefined,
      entryFileNames: 'index.js',  // Main JS file (like App.js)
      chunkFileNames: 'chunk-[hash].js',  // For dynamic imports (if any)
      assetFileNames: '[name].[ext]',  // Asset file names (CSS, images, etc.)
    },
  },
})
