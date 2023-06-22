import Link from 'next/link'

const Board = () => {

  return <div className="absolute top-0">
    <ul className="flex flex-column gap-x-2">
      <li>Boards:</li>
      <li><Link href="/technology" className="hover:text-white">/g/</Link></li>
      <li><Link href="/videogames" className="hover:text-white">/v/</Link></li>
      <li><Link href="/" className="hover:text-white ml-2">[Back to home]</Link></li>
    </ul>
  </div>
}

export default Board;