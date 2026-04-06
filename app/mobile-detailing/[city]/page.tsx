import fs from 'fs';
import path from 'path';
import { Metadata } from 'next';
import Link from 'next/link';

interface CityData {
  city: string;
  state: string;
  slug: string;
  title: string;
  description: string;
  services: string[];
  price_estimate: string;
  turnaround_time: string;
  why_us: string[];
  faqs: { question: string; answer: string }[];
}

export async function generateStaticParams() {
  const dataDir = path.join(process.cwd(), 'data/cities');
  const cityFiles = fs.readdirSync(dataDir).filter(file => file.endsWith('.json') && file !== 'cities-index.json');
  return cityFiles.map(file => ({
    city: file.replace('.json', '')
  }));
}

export async function generateMetadata({ params }: { params: { city: string } }): Promise<Metadata> {
  const dataPath = path.join(process.cwd(), `data/cities/${params.city}.json`);
  if (!fs.existsSync(dataPath)) return { title: 'City Not Found' };
  
  const cityData: CityData = JSON.parse(fs.readFileSync(dataPath, 'utf8'));
  return {
    title: cityData.title,
    description: cityData.description,
  };
}

export default function CityPage({ params }: { params: { city: string } }) {
  const dataPath = path.join(process.cwd(), `data/cities/${params.city}.json`);
  if (!fs.existsSync(dataPath)) return <div>City not found</div>;
  
  const cityData: CityData = JSON.parse(fs.readFileSync(dataPath, 'utf8'));

  return (
    <div className="max-w-4xl mx-auto py-12 px-4">
      <header className="mb-12">
        <Link href="/mobile-detailing" className="text-blue-600 hover:underline mb-4 block">← All Cities</Link>
        <h1 className="text-5xl font-extrabold mb-4">{cityData.city} Mobile Detailing</h1>
        <p className="text-xl text-gray-700 leading-relaxed">{cityData.description}</p>
      </header>

      <section className="grid grid-cols-1 md:grid-cols-2 gap-12 mb-12">
        <div className="bg-white p-8 rounded-xl shadow-sm border">
          <h2 className="text-2xl font-bold mb-6">Our Services</h2>
          <ul className="space-y-3">
            {cityData.services.map((service, idx) => (
              <li key={idx} className="flex items-center">
                <span className="text-blue-500 mr-3">✓</span> {service}
              </li>
            ))}
          </ul>
        </div>
        <div className="bg-blue-50 p-8 rounded-xl border border-blue-100">
          <h2 className="text-2xl font-bold mb-6">Pricing & Time</h2>
          <div className="space-y-6">
            <div>
              <h3 className="font-semibold text-gray-600 uppercase text-sm tracking-wider">Estimated Price</h3>
              <p className="text-3xl font-bold text-blue-800">{cityData.price_estimate}</p>
            </div>
            <div>
              <h3 className="font-semibold text-gray-600 uppercase text-sm tracking-wider">Typical Time</h3>
              <p className="text-3xl font-bold text-blue-800">{cityData.turnaround_time}</p>
            </div>
          </div>
        </div>
      </section>

      <section className="mb-12">
        <h2 className="text-3xl font-bold mb-8">Why Choose Our {cityData.city} Team?</h2>
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-6">
          {cityData.why_us.map((reason, idx) => {
            const parts = reason.split(':');
            return (
              <div key={idx} className="p-6 bg-gray-50 rounded-lg">
                <p className="font-semibold text-lg">{parts[0]}</p>
                {parts[1] && <p className="text-gray-600 mt-2">{parts[1].trim()}</p>}
              </div>
            );
          })}
        </div>
      </section>

      <section className="mb-12">
        <h2 className="text-3xl font-bold mb-8">Frequently Asked Questions</h2>
        <div className="space-y-6">
          {cityData.faqs.map((faq, idx) => (
            <div key={idx} className="border-b pb-6 last:border-0">
              <h3 className="text-xl font-bold mb-2">{faq.question}</h3>
              <p className="text-gray-700 leading-relaxed">{faq.answer}</p>
            </div>
          ))}
        </div>
      </section>

      <div className="bg-blue-600 text-white p-12 rounded-2xl text-center shadow-xl">
        <h2 className="text-3xl font-bold mb-4">Ready to Refresh Your Car?</h2>
        <p className="text-xl mb-8 opacity-90">Book your mobile detail today and experience the difference.</p>
        <button className="bg-white text-blue-600 px-10 py-4 rounded-full font-bold text-lg hover:bg-gray-100 transition-colors shadow-lg">
          Get Your Free Quote
        </button>
      </div>
    </div>
  );
}
