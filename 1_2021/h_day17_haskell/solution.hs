import Data.List


tax1 = 150
tax2 = 193
tay1 = -86
tay2 = -136

sumTo n = round (m/2 * (m+1)) where m = fromIntegral n

pos xv yv n = ((sumTo xv) - (sumTo (max 0 (xv-n))), (sumTo yv) - (sumTo (yv-n)))

inTA (x,y) = x >= tax1 && x <= tax2 && y <= tay1 && y >= tay2

poss xv yv = takeWhile (\(x,y) -> x <= tax2 && y >= tay2) [pos xv yv n | n <- [1..]]

rev (a,b) = (b,a)
sortlast t = map rev (sort (map rev t))

val = filter (\t -> inTA (last t)) (filter (\t -> length t /= 0) [ poss gx gy | gx <- [0..200], gy <- [-150..400]])

splitMaxY ((x,y):(x',y'):r) | y >= y' = [(x',y')]
                            | otherwise = (x,y) : splitMaxY ((x',y'):r)  

maxY = snd (last (sortlast (concat val)))

main :: IO ()
main = do
 putStr "Part 1: "
 print maxY
 putStr "Part 2: "
 print (length val)
 print "done."
