import { Metadata } from 'next';
import Link from 'next/link';

export const metadata: Metadata = {
  title: 'Local Home & Auto Services Near You | Professional Mobile Professionals',
  description: 'Find top-rated local services in your city. Mobile detailing, appliance repair, and more. Certified, reliable, and convenient.',
};

export default function Home() {
  return (
    <main className="max-w-4xl mx-auto py-24 px-4 text-center">
      <h1 className="text-6xl font-extrabold mb-8 tracking-tight">Professional Services, <span className="text-blue-600">Delivered.</span></h1>
      <p className="text-2xl text-gray-600 mb-12 max-w-2xl mx-auto leading-relaxed">
        Expert help for your home and car, right at your doorstep. Compare local pros and get free quotes in seconds.
      </p>
      
      <div className="grid grid-cols-1 md:grid-cols-2 gap-8 max-w-2xl mx-auto">
        <Link 
          href="/mobile-detailing" 
          className="p-10 border rounded-3xl hover:border-blue-600 hover:shadow-2xl transition-all bg-white group text-left"
        >
          <div className="text-5xl mb-6">🚗</div>
          <h2 className="text-2xl font-bold mb-2 group-hover:text-blue-600">Mobile Detailing</h2>
          <p className="text-gray-600">Interior/exterior car care at your home or office.</p>
        </Link>
        <div 
          className="p-10 border rounded-3xl bg-gray-50 opacity-60 text-left"
        >
          <div className="text-5xl mb-6">🧺</div>
          <h2 className="text-2xl font-bold mb-2">Appliance Repair</h2>
          <p className="text-gray-600 italic">Expanding soon to new cities...</p>
        </div>
      </div>
      
      <div className="mt-24 text-gray-400 font-medium tracking-widest uppercase text-sm">
        Trusted in 20+ Cities Nationwide
      </div>
    </main>
  );
}
