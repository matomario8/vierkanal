import Image from 'next/image'
import Link from 'next/link'
import { Inter } from 'next/font/google'
import HeaderArt from '@/components/HeaderArt'

const inter = Inter({ subsets: ['latin'] })

//Pull the board title
//Load an image url

export default function Home() {
  return (
    <main
      className={`flex min-h-screen flex-col items-center p-24 ${inter.className}`}
    >
      
      <HeaderArt imgurl="/assets/bildschirmfoto.png"></HeaderArt>

      <Link href="/technology">/g/</Link>
      
    </main>
  )
}
