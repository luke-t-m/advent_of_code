{-# LANGUAGE NoMonomorphismRestriction #-}
{-# LANGUAGE FlexibleContexts          #-}
{-# LANGUAGE TypeFamilies              #-}

import Data.List
import Data.List.Split
import Diagrams.Prelude
import Diagrams.Backend.SVG.CmdLine

foldUp foldY pnt@(y,x) | y > foldY = ((foldY - (y - foldY)), x)
                 | otherwise = pnt

foldLeft foldX pnt@(y,x) | x > foldX = (y, (foldX - (x - foldX)))
                   | otherwise = pnt

conv (x:[y]) = (y,x)


fold "y" foldY pnts = nub (map (foldUp foldY) pnts)
fold "x" foldX pnts = nub (map (foldLeft foldX) pnts)

folder pnts [] = pnts
folder pnts ((n,t):fs) = folder (fold t (read n) pnts) fs


-- make and run at terminal with ./solution_part2 -o points.svg -w 400

main = do
 input <- readFile "input.txt"
 let u = map (conv . splitOn "=" . last . splitOn " ") (lines (last (splitOn "\n\n" input)))
 let i = head (splitOn "\n\n" input)
 let points = map (conv . (map read) . splitOn ",") (lines i)
 let diag = flip atPoints (repeat (circle 0.8 # fc black)) $ map p2 $ (folder points u) :: Diagram B
 mainWith diag
