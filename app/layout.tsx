import type { Metadata } from 'next'
import { Inter } from 'next/font/google'
import './globals.css'

const inter = Inter({ subsets: ['latin'] })

export const metadata: Metadata = {
  title: { template: '%s | ApplianceRepairLocal.com', default: 'Find the Best Appliance Repair Companies Near You' },
  description: 'Find the best local appliance repair companies. Real prices on diagnostics, same-day repairs, refrigerator repair, washer repair, and premium appliance service. Free quotes.',
  metadataBase: new URL(process.env.NEXT_PUBLIC_SITE_URL || 'https://appliance-repair-local.vercel.app'),
}

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body className={`${inter.className} bg-gray-50 text-gray-900`}>
        <header className="bg-white border-b border-gray-200 sticky top-0 z-50">
          <div className="max-w-6xl mx-auto px-4 py-4 flex items-center justify-between">
            <a href="/" className="flex items-center gap-2 font-bold text-xl text-red-700">
              <span className="text-2xl">🔧</span>
              <span>Appliance Repair Local</span>
            </a>
            <nav className="hidden md:flex items-center gap-6 text-sm text-gray-600">
              <a href="/appliance-repair" className="hover:text-red-700 transition-colors">Find Repair Pros by City</a>
            </nav>
            <a href="#get-quotes" className="bg-red-600 text-white px-5 py-2 rounded-lg text-sm font-semibold hover:bg-red-700 transition-colors">
              Get Free Quotes
            </a>
          </div>
        </header>
        {children}
      </body>
    </html>
  )
}
