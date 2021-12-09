import Data.List
import Data.List.Split

dalist = [((\(g,y,x) -> y /= g),(1,0)), 
          ((\(g,y,x) -> y /= 0),(-1,0)),
          ((\(g,y,x) -> x /= g),(0,1)),
          ((\(g,y,x) -> x /= 0),(0,-1))]

makelist g (y,x) = map snd (filter (\t -> (fst t) ((length g - 1),y,x)) dalist)  

isLow g (y,x) = and [(g!!y!!x) < (g!!(y+ym)!!(x+xm)) | (ym,xm) <- (makelist g (y,x))]

spread g (y,x) = (y,x):[(y+ym,x+xm) | (ym,xm) <- (makelist g (y,x)),
                 (g!!y!!x) < g!!(y+ym)!!(x+xm) && g!!(y+ym)!!(x+xm) /= 9]

spreader g l
 | n == l = n
 | otherwise = spreader g n
  where n =  nub $ concat (map (spread g) l)

main :: IO ()
main = do
 input <- readFile "input.txt"
 let g = map (map (\y -> read [y]::Int)) (lines input)
 let poss = [ (y,x) | y <- [0..(length g-1)], x <- [0..(length (head g)-1)]]
 print (sum $ map (\(y,x) -> (g!!y!!x)+1) (filter (isLow g) poss)) -- part 1
 print (product $ fst $ splitAt 3 $ reverse $ sort $ map length (map (\t -> spreader g [t]) poss)) -- part 2
 print "done."
