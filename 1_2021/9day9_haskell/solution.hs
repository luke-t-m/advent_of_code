import Data.List
import Data.List.Unique
import Data.List.Split


c1 y x g@(r:rs) | y /= (length g-1) = (1,0):(c2 y x g)
                | otherwise = (c2 y x g)
c2 y x g@(r:rs) | y /= 0 = (-1,0):(c3 y x g)
                | otherwise = (c3 y x g)
c3 y x g@(r:rs) | x /= (length r-1) = (0,1):(c4 y x g)
                | otherwise = (c4 y x g)
c4 y x g@(r:rs) | x /= 0 = [(0,-1)]
                | otherwise = []

isLow g y x = and [(g!!y!!x) < (g!!(y+ym)!!(x+xm)) | (ym,xm) <- (c1 y x g)]

spread g (y,x) = (y,x):[(y+ym,x+xm) | (ym,xm) <- (c1 y x g), (g!!y!!x) < (g!!(y+ym)!!(x+xm)) && (g!!(y+ym)!!(x+xm)) /= 9]


spreader g l
 | n == l = n
 | otherwise = spreader g n
  where n =  nub (concat (map (spread g) l))


main :: IO ()
main = do
 input <- readFile "input.txt"
 let g = map (map (\y -> read [y]::Int)) (lines input)
 print (sum [(g!!y!!x)+1 | y <- [0..(length g-1)], x <- [0..(length (head g)-1)] , isLow g y x])
 print (product (fst (splitAt 3 (reverse $ sort (map length [spreader g [(y,x)] | y <- [0..(length g-1)], x <- [0..(length (head g)-1)]])))))
 print "done."
