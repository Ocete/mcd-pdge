//package org.apache.hadoop.examples;
package uam;
import java.io.IOException;
import java.util.*;
import java.lang.Math;

import org.apache.hadoop.conf.*;
import org.apache.hadoop.mapreduce.*;
import org.apache.hadoop.io.*;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class Players {

  public static class PlayersMapper extends Mapper<Object, Text, Text, IntWritable>{

    private final static IntWritable age = new IntWritable();
    private Text team = new Text();

    public void map(Object key, Text value, Context context)
        throws IOException, InterruptedException {
      String[] data = value.toString().split(",");
      team.set(data[1]);
      age.set(Integer.parseInt(data[2]));
      context.write(team, age);
    }
  }

  public static class PlayersReducer extends Reducer<Text, IntWritable, Text, Iterable<FloatWritable>> {

    private FloatWritable mean = new FloatWritable();
    private FloatWritable std = new FloatWritable();

    public void reduce(Text key, Iterable<IntWritable> values, Context context) throws IOException, InterruptedException {
      float sum = 0;
      float sum_squared = 0;
      int n_elems = 0;
      
      for (IntWritable val : values) {
        n_elems++;
        sum += val.get();
        sum_squared += val.get() * val.get();
      }

      mean.set(sum / n_elems);
      std.set((float)Math.sqrt(sum_squared / n_elems - mean.get() * mean.get()));

      FloatWritable result[] = {mean, std};
      context.write(key, Arrays.asList(result));
    }
  }

  public static void main(String[] args) throws Exception {
    Configuration conf = new Configuration();

    /*String[] otherArgs = new GenericOptionsParser(conf, args).getRemainingArgs();
    if (otherArgs.length != 2) {
      System.err.println("Usage: wordcount <in> <out>");
      System.exit(2);
    }*/

    @SuppressWarnings("deprecation")
    Job job = new Job(conf, "wordcount");
    job.setJarByClass(Players.class);
    job.setMapperClass(PlayersMapper.class);
    // job.setCombinerClass(PlayersReducer.class);
    job.setReducerClass(PlayersReducer.class);
    job.setOutputKeyClass(Text.class);
    job.setOutputValueClass(IntWritable.class);

    FileInputFormat.addInputPath(job, new Path(args[0]));
    FileOutputFormat.setOutputPath(job, new Path(args[1]));

    System.exit(job.waitForCompletion(true) ? 0 : 1);
  }
}
