import Data.List
import Data.List.Split


foldUp foldY pnt@(y,x) | y > foldY = ((foldY - (y - foldY)), x)
                 | otherwise = pnt

foldLeft foldX pnt@(y,x) | x > foldX = (y, (foldX - (x - foldX)))
                   | otherwise = pnt

conv (x:[y]) = (y,x)



fold "y" foldY pnts = nub (map (foldUp foldY) pnts)
fold "x" foldX pnts = nub (map (foldLeft foldX) pnts)

folder :: [(Int,Int)] -> [(String,String)] -> [(Int,Int)]
folder pnts [] = pnts
folder pnts ((n,t):fs) = folder (fold t (read n) pnts) fs

main :: IO ()
main = do
 input <- readFile "input.txt"
 let u = map (conv . splitOn "=" . last . splitOn " ") (lines (last (splitOn "\n\n" input)))
 let i = head (splitOn "\n\n" input)
 let points = map (conv . (map read) . splitOn ",") (lines i) :: [(Int,Int)]
 print (length (folder points [head u]))



