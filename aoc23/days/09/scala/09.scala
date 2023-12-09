import scala.io.Source

object run {
    def main(args: Array[String]) = {
        val source = Source.fromFile("../input")
        val (l, r) = (for line <- source.getLines() yield solve(parse(line))).toArray.unzip
        println(f"Part one: ${r.sum}, Part two: ${l.sum} ")
        source.close()
    }

    def parse(line: String): Array[Int] = line.split(" ").map(i => i.toInt)

    def solve(ns : Array[Int]): (Int, Int) = if (ns.forall(_ == 0)) (0, 0) else {
        val (l, r) = solve(ns.zip(ns.tail).map((i, j) => j - i))
        return (ns.head - l, ns.last + r)
    }
}