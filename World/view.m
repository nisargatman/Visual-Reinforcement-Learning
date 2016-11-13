fid = fopen('pic_red.txt');
tline = fgetl(fid);
image2 = [];
n = 1;
while ischar(tline)
    image2 = [image2 str2num(tline)];
    tline = fgetl(fid);
end

image2 = reshape(image2, [640,480]);
imtool(image', [0 255])
fclose(fid);

fid = fopen('pic_green.txt');
tline = fgetl(fid);
image3 = [];
n = 1;
while ischar(tline)
    image3 = [image3 str2num(tline)];
    tline = fgetl(fid);
end

image3 = reshape(image3, [640,480]);
imtool(image', [0 255])
fclose(fid);

fid = fopen('pic_blue.txt');
tline = fgetl(fid);
image = [];
n = 1;
while ischar(tline)
    image = [image str2num(tline)];
    tline = fgetl(fid);
end

image = reshape(image, [640,480]);
imtool(image', [0 255])
fclose(fid);