#!/usr/bin/env ruby
sender = ARGV[0].scan(/\[from:(.+?)\]/).join
receiver = ARGV[0].scan(/\[to:(\+{0,1}\d+)\]/).join
flags = ARGV[0].scan(/\[flags:(.+?)\]/).join

puts "#{sender},#{receiver},#{flags}"

