import Data.List
import Data.List.Split
import Data.Maybe
import qualified Data.Heap as Heap
import qualified Data.Set as Set

dijkstra :: [[Int]] -> Set.Set (Int,Int) -> (Heap.MinHeap (Int,(Int,Int))) -> Int
dijkstra grid seen tovisit
 | y==maxy && x==maxx = w
 | otherwise = dijkstra grid (Set.union (Set.fromList neighbours) seen) (foldl (\y z -> Heap.insert z y) b [((w+(grid!!ny!!nx)),(ny,nx)) | (ny,nx) <- neighbours])
  where ((w,(y,x)),b) = fromJust (Heap.view tovisit)
        neighbours = filter (\t@(ty,tx) -> not (Set.member t seen) && ty>=0 && ty<=maxy && tx>=0 && tx<=maxx) (map (\(my,mx) -> (y+my, x+mx)) [(1,0),(-1,0),(0,1),(0,-1)])
        maxy = (length grid) -1
        maxx = (length (head grid))-1


makedij grid = (0,(0,0)) : tail [(10000,(y,x)) | y <- [0..maxy], x <- [0..maxx]]
 where maxy = (length grid) -1
       maxx = (length (head grid))-1

makept2 x = concat (take 5 (iterate (map increase) (map (\t -> concat (take 5 (iterate increase t))) x)))

increase x = map f x
 where f 9 = 1
       f n = n+1

main :: IO ()
main = do
 input <- readFile "input.txt"
 let x = map (map read . tail . splitOn "") (lines input) :: [[Int]]
     toHeap i = Heap.fromList (makedij i) :: Heap.MinHeap (Int,(Int,Int))
     solve i = dijkstra i (Set.fromList []) (toHeap i)
 putStr "Part 1: "
 print (solve x)
 putStr "Part 2: "
 print (solve (makept2 x))
 print "done."
