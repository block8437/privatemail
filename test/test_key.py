from enc import public
key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDK4NE/jvgA790Ni/P/+5MYzE7GEgU8A/OPrn9qnRCDv2gIrjwuzRWfb0dhdJBbv/IhV28vBK0Pgce1FTTFCJKLDmhJaRUD7szQh1wjXZR3tRdSNDrpXH+7mnPBg2HoNFHaELFSVIeBIqvIS3gHoVQTLdQ1s2w+VWe/vhtmmzAh/cQwvjo7Bd+id6kik7MApFsfi/4+benNWg/91HyWYQk6yd04++45TTud/ftW7LlFrQHAZ1jlBE6Sh11KVxhgjnyVxWckOHZRgboQuFFczcvNp+N/ucZO+6u6ztJr2vLNjlpY4SR6Q9I3mRS28z1gwKw0yeHPxqlSVsOBK63gT8RZ"
print public.decode_key(key)
