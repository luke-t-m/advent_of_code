import System.IO
import Data.List.Split
import Data.List.Unique


points diag ((s:[t]):[u:[v]])
 | m == 1/0 || m == 0 =  [ (a,b) | a <- [x2..x1], b <- [y2..y1]]
 | diag == True && (m == 1 || m == -1) = [ (x2+a,y2+m*a) | a <- [0..(x1-x2)]]
 | otherwise = []
  where
   (x1,y1) = max (read s, read t) (read u, read v)
   (x2,y2) = min (read s, read t) (read u, read v)
   m = (y1 - y2) / (x1 - x2) 

solve x diag = length (repeated (concat (map (points diag) x)))

main :: IO ()
main = do
 input <- readFile "input.txt"
 let x = map (map ( splitOn ",") . splitOn " -> ") (lines input)
 print (solve x False)
 print (solve x True)
 print "done."
