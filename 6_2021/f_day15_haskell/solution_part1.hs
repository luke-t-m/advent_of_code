import Data.List
import Data.List.Split
import Data.Maybe



rev (a,b) = (b,a)
rsort x = map rev (sort (map rev x))

dijkstra grid dij@(((y,x),w):b)
 | y == maxy && x == maxx = w
 | otherwise = dijkstra grid  (rsort (sort [ ((ny,nx), min (w+(grid!!ny!!nx)) (fromJust (lookup (ny,nx) dij))) | (ny,nx) <- neighbours] ++ filter (\((ty,tx),w) -> (not ((ty,tx) `elem` neighbours))) b))
  where
        neighbours = filter indij (map (\(my,mx) -> (y+my, x+mx)) [(1,0),(-1,0),(0,1),(0,-1)])
        indij c = length (filter (\((y,x),w) -> (y,x) == c) dij) /= 0
        maxy = (length grid) -1
        maxx = (length (head grid))-1

makedij grid = ((0,0),0) : tail [((y,x),1000) | y <- [0..maxy], x <- [0..maxx]]
 where maxy = (length grid) -1
       maxx = (length (head grid))-1

main :: IO ()
main = do
 input <- readFile "input.txt"
 let x = map (map read . tail . splitOn "") (lines input) :: [[Int]]
 print (dijkstra x (makedij x))

 putStr "Part 1: "
 print (dijkstra x (makedij x))
 putStr "Part 2: "
 print "not happening pal"
 print "done."



