/** import node */
import { resolve } from 'path'
/** import vite */
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  // import @/の対応
  resolve: {
    alias: {
      '@': resolve(__dirname, 'src')
    }
  },
  // docker host用
  server: {
    host: true
  },
})