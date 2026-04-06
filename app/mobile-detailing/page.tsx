import type { Metadata } from 'next'
import Link from 'next/link'
import fs from 'fs'
import path from 'path'

export const metadata: Metadata = {
  title: 'Local Mobile Detailing Services | Professional Car Care at Your Door',
  description: 'Find top-rated mobile detailing services in your city. Interior detailing, exterior wash, ceramic coating, and more.',
}

export default function MobileDetailingPage() {
  const dataDir = path.join(process.cwd(), 'data/cities');
  const cityFiles = fs.readdirSync(dataDir).filter(file => file.endsWith('.json'));
  
  const cities = cityFiles.map(file => {
    const filePath = path.join(dataDir, file);
    const fileContent = fs.readFileSync(filePath, 'utf8');
    return JSON.parse(fileContent);
  });

  return (
    <main className="max-w-4xl mx-auto py-12 px-4">
      <h1 className="text-4xl font-bold mb-8">Professional Mobile Detailing by City</h1>
      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
        {cities.map((city) => (
          <Link
            key={city.slug}
            href={`/mobile-detailing/${city.slug}`}
            className="p-6 border rounded-lg hover:shadow-lg transition-shadow bg-white"
          >
            <h2 className="text-xl font-semibold">{city.city}, {city.state}</h2>
            <p className="text-gray-600 mt-2">Mobile detailing at your doorstep.</p>
          </Link>
        ))}
      </div>
    </main>
  );
}
