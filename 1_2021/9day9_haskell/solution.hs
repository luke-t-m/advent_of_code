import Data.List
import Data.List.Split


dalist = [((\(g,y,x) -> y /= g),(1,0)), 
          ((\(g,y,x) -> y /= 0),(-1,0)),
          ((\(g,y,x) -> x /= g),(0,1)),
          ((\(g,y,x) -> x /= 0),(0,-1))]

makelist y x g = map snd (filter (\t -> (fst t) ((length g - 1),y,x)) dalist)  

isLow g y x = and [(g!!y!!x) < (g!!(y+ym)!!(x+xm)) | (ym,xm) <- (makelist y x g)]

spread g (y,x) = (y,x):[(y+ym,x+xm) | (ym,xm) <- (makelist y x g), (g!!y!!x) < (g!!(y+ym)!!(x+xm)) && (g!!(y+ym)!!(x+xm)) /= 9]


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
