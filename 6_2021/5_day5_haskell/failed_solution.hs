import System.IO
import Data.List
import Data.List.Split


lineEq :: [Float] -> [[String]] -> (Float -> Float -> Bool)
lineEq vG ((s:t:[]):(u:v:[]):[])
 | m == 1/0 = \x -> \y -> x == a && lims x y -- vertical line
 | m `elem` vG = \x -> \y -> y - b == m * (x - a) && lims x y -- other valid gradients
 | otherwise = \x -> \y -> False
  where
   a = read s
   b = read t
   c = read u
   d = read v
   m = (d - b) / (c - a) 
   lims x y = x >= min a c && x <= max a c && y >= min d b && y <= max d b -- point is within ends of line



max3 a b c = max a (max b c)
min3 a b c = min a (min b c)

edges bx by sx sy [] = bx:by:sx:[sy]
edges bx by sx sy (((s:t:[]):(u:v:[]):[]):xs) = edges (max3 bx a c) (max3 by b d) (min3 sx a c) (min3 sy b d) xs
 where
  a = read s
  b = read t
  c = read u
  d = read v

trues x = length (filter (==True) x)

toConsider vG [] = []
toConsider vG (((s:t:[]):(u:v:[]):[]):xs)
 | m == 1/0 || m `elem` vG = [ (x,y) | x <- [sx..bx], y <- [sy..by]] ++ toConsider vG xs
 | otherwise = toConsider vG xs
  where
   a = read s
   b = read t
   c = read u
   d = read v
   sx = min a c
   bx = max a c
   sy = min b d
   by = max b d
   m = (d - b) / (c - a) 



scanPoints (bx:by:sx:[sy]) eqs pts = [ trues (map (\f -> f a b) eqs) >= 2 | (a,b) <- pts ]

final vG x eds = scanPoints eds (map (lineEq vG) x) (nub (toConsider vG x))

main :: IO ()
main = do
 input <- readFile "input.txt"
 let x = map (map ( splitOn ",") . splitOn " -> ") (lines input)
 let eds = edges 0 0 0 0 x
 print (final [0] x eds)


