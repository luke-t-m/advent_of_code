import Data.List

tax1 = 150
tax2 = 193
tay1 = -86
tay2 = -136

poss xv yv = takeWhile (\(x,y) -> x <= tax2 && y >= tay2) [pos xv yv n | n <- [1..]]
 where pos xv yv n = ((sumTo xv) - (sumTo (max 0 (xv-n))), (sumTo yv) - (sumTo (yv-n)))
       sumTo n = round (m/2 * (m+1)) where m = fromIntegral n

val = filter (\t -> inTA (last t)) (filter (\t -> length t /= 0) [ poss gx gy | gx <- [17..193], gy <- [-136..136]])
 where inTA (x,y) = x >= tax1 && x <= tax2 && y <= tay1 && y >= tay2

maxY = snd (last (sortlast (concat val)))
 where sortlast t = map rev (sort (map rev t))
       rev (a,b) = (b,a)

main :: IO ()
main = do
 putStr "Part 1: "
 print maxY
 putStr "Part 2: "
 print (length val)
 print "done."
